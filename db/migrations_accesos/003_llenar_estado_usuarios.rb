require 'sequel'

Sequel.migration do
  up do
    Sequel.connect('sqlite://db/accesos.db')
    #Sequel.connect('mysql2://localhost/accesos?user=root&password=123')
		DB.transaction do
	  	file = File.new('db/data/estado_usuarios.txt', 'r')
			while (line = file.gets)
				nombre = line.strip
				DB[:estado_usuarios].insert(nombre: nombre)
      end
		end
  end

	down do
		DB = Sequel.connect('sqlite://db/accesos.db')
		#DB = Sequel.connect('mysql2://localhost/gestion?user=root&password=123')
    DB[:estado_usuarios].delete
	end
end