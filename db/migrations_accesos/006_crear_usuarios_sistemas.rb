require 'sequel'

Sequel.migration do
  up do
    create_table(:usuarios_sistemas) do
      primary_key :id
    end

    alter_table(:usuarios_sistemas) do
      add_foreign_key :usuario_id, :usuarios
      add_foreign_key :sistema_id, :sistemas
    end
	end

  down do
    drop_column :usuarios_sistemas, :usuario_id
    drop_column :usuarios_sistemas, :sistema_id
    drop_table(:usuarios_sistemas)
	end
end
