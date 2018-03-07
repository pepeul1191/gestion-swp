require 'sequel'

Sequel.migration do
  up do
    create_table(:accesos) do
      primary_key :id
      Datetime :momento, null: false
    end

    alter_table(:accesos) do
      add_foreign_key :usuario_id, :usuarios
    end
	end

  down do
    drop_column :accesos, :usuario_id
    drop_table(:accesos)
	end
end
