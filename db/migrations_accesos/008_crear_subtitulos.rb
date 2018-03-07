require 'sequel'

Sequel.migration do
  up do
    create_table(:subtitulos) do
      primary_key :id
      String :nombre, null: false, size: 25
    end

    alter_table(:subtitulos) do
      add_foreign_key :modulo_id, :modulos
    end
	end

  down do
    drop_column :subtitulos, :modulo_id
    drop_table(:subtitulos)
	end
end
