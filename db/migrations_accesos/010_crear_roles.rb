require 'sequel'

Sequel.migration do
  up do
    create_table(:roles) do
      primary_key :id
      String :nombre, null: false, size: 20
    end

    alter_table(:roles) do
      add_foreign_key :sistema_id, :sistemas
    end
	end

  down do
    drop_column :roles, :sistema_id
    drop_table(:roles)
	end
end
