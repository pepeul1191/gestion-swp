require 'sequel'

Sequel.migration do
  up do
    create_table(:roles_permisos) do
      primary_key :id
    end

    alter_table(:roles_permisos) do
      add_foreign_key :rol_id, :roles
      add_foreign_key :permiso_id, :permisos
    end
	end

  down do
    drop_column :roles_permisos, :rol_id
    drop_column :roles_permisos, :permiso_id
    drop_table(:roles_permisos)
	end
end
