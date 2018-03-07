require 'sequel'

Sequel.migration do
  up do
    create_table(:usuarios) do
      primary_key :id
      String :usuario, null: false, size: 20
      String :contrasenia, null: false, size: 60
      String :correo, null: false, size: 40
    end

    alter_table(:usuarios) do
      add_foreign_key :estado_usuario_id, :usuarios
    end
	end

  down do
    drop_column :usuarios, :estado_usuario_id
    drop_table(:usuarios)
	end
end
