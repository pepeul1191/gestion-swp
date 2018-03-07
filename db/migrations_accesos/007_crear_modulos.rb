require 'sequel'

Sequel.migration do
  up do
    create_table(:modulos) do
      primary_key :id
      String :nombre, null: false, size: 20
      String :url, null: false, size: 40
      String :icono, null: false, size: 25
    end

    alter_table(:modulos) do
      add_foreign_key :sistema_id, :sistemas
    end
	end

  down do
    drop_column :modulos, :sistema_id
    drop_table(:modulos)
	end
end
