require 'sequel'

Sequel.migration do
  up do
    create_table(:usuarios_roles) do
      primary_key :id
    end

    alter_table(:usuarios_roles) do
      add_foreign_key :usuario_id, :usuarios
      add_foreign_key :rol_id, :roles
    end
	end

  down do
    drop_column :usuarios_roles, :usuario_id
    drop_column :usuarios_roles, :rol_id
    drop_table(:usuarios_roles)
	end
end
