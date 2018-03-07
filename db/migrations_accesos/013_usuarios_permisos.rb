require 'sequel'

Sequel.migration do
  up do
    create_table(:usuarios_permisos) do
      primary_key :id
    end

    alter_table(:usuarios_permisos) do
      add_foreign_key :usuario_id, :usuarios
      add_foreign_key :permiso_id, :permisos
    end
	end

  down do
    drop_column :usuarios_permisos, :usuario_id
    drop_column :usuarios_permisos, :permiso_id
    drop_table(:usuarios_permisos)
	end
end
