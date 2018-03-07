require 'sequel'

Sequel.migration do
  up do
    create_table(:permisos) do
      primary_key :id
      String :nombre, null: false, size: 20
      String :llave, null: false, size: 25
    end

    alter_table(:permisos) do
      add_foreign_key :sistema_id, :sistemas
    end
	end

  down do
    drop_column :permisos, :sistema_id
    drop_table(:permisos)
	end
end
