require 'sequel'

Sequel.migration do
  up do
    create_table(:sistemas) do
      primary_key :id
      String :nombre, null: false, size: 25
      String :version, null: false, size: 10
      String :repositorio, null: false, size: 50
    end
	end

  down do
    drop_table(:sistemas)
	end
end