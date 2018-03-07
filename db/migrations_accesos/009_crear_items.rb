require 'sequel'

Sequel.migration do
  up do
    create_table(:items) do
      primary_key :id
      String :nombre, null: false, size: 20
      String :url, null: false, size: 40
    end

    alter_table(:items) do
      add_foreign_key :subtitulo_id, :subtitulos
    end
	end

  down do
    drop_column :items, :subtitulo_id
    drop_table(:items)
	end
end
