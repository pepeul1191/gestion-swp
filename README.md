## Python3 Tornado

Requisitos de software previamente instalado:

+ Python 3.5
+ Python PIP

### Descipción

En caso de usar el servicio en python:

    $ sudo pip install virtualenv
    $ virtualenv -p python3 <<nombre_ambiente>>
    $ cd <<nombre_ambiente>>
    $ source bin/activate

Arrancar servidor Torando

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ python app.py

### Migraciones

Ejemplo de migración con distintos motores de base de datos:

    $ sequel -m db/migrations -M #version postgres://host/database
    $ sequel -m db/migrations -M #version sqlite://db/gestion.db
    $ sequel -m db/migrations -M #version mysql://root:123@localhost/gestion

Ejecutar el 'down' de las migraciones de la última a la primera:

    $ sequel -m db/migrations -M 0 mysql://root:123@localhost/gestion

Ejecutar el 'up' de las migraciones hasta un versión especifica:

    $ sequel -m db/migrations -M #version mysql://root:123@localhost/gestion


Migraciones:

    $ sequel -m db/migrations_ubicaciones -M 3 sqlite://db/ubicaciones.db

Crear Vista de distrito/provincia/departamento

    MySQL
    >> CREATE VIEW vw_distrito_provincia_departamento AS select DI.id AS id, PA.id AS pais_id, concat(DI.nombre,', ',PR.nombre,', ',DE.nombre) AS nombre from ((distritos DI join provincias PR on((DI.provincia_id = PR.id))) join departamentos DE on((PR.departamento_id = DE.id))) join paises PA on((DE.pais_id = PA.id)) limit 2000;
    SQLite
    >> CREATE VIEW vw_distrito_provincia_departamento AS select DI.id AS id, PA.id AS pais_id,  DI.nombre || ', '  || PR.nombre || ', '  || DE.nombre AS nombre from ((distritos DI join provincias PR on((DI.provincia_id = PR.id))) join departamentos DE on((PR.departamento_id = DE.id))) join paises PA on((DE.pais_id = PA.id)) limit 2000;

Tipos de Datos de Columnas

+ :string=>String
+ :integer=>Integer
+ :date=>Date
+ :datetime=>[Time, DateTime].freeze,
+ :time=>Sequel::SQLTime,
+ :boolean=>[TrueClass, FalseClass].freeze,
+ :float=>Float
+ :decimal=>BigDecimal
+ :blob=>Sequel::SQL::Blob

### Fuentes:

+ http://www.tornadoweb.org/en/stable/
+ https://github.com/pepeul1191/tornado-animalitos
+ https://simplapi.wordpress.com/2014/03/26/python-tornado-and-decorator/
+ https://stackoverflow.com/questions/47010763/tornado-asynchronous-actions-in-custom-decorator

Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]
