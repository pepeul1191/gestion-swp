require 'sequel'

Sequel.migration do
  up do
    create_table(:estado_usuarios) do
      primary_key :id
      String :nombre, null: false, size: 15
    end
	end

  down do
    drop_table(:estado_usuarios)
	end
end