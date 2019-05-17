from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

db_string = 'postgres://Llang8:Cod1ngTemple32@dealership.cgsf4ufm4fjo.us-east-2.rds.amazonaws.com:5432/dealership'

db = create_engine(db_string) # Create connection to the database

Base = declarative_base()


# Creation of Database Models for Object Relational Mapper -- ORM
class Salesperson(Base):
    __tablename__ = "salesperson"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(255))

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(255))

class Mechanic(Base):
    __tablename__ = "mechanic"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(255))

class CustomerCar(Base):
    __tablename__ = "customer_car"

    serial_number = Column(String(255), primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))

    customer = relationship('Customer', backref='customer')

class Invoice(Base):
    __tablename__ = "invoice"

    id = Column(Integer, primary_key=True)
    serial_number = Column(String(255), ForeignKey('inventory_car.serial_number'))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    salesperson_id = Column(Integer,ForeignKey('salesperson.id'))
    amount = Column(Numeric(9,2))
    invoice_date = Column(Date)

    inventory_car = relationship('InventoryCar', backref='inventory_car')
    customer = relationship('Customer', backref='customer')
    salesperson = relationship('Salesperson', backref='salesperson')

class Service(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True)
    serial_number = Column(String(255), ForeignKey('customer_car.serial_number'))
    mechanic_id = Column(Integer, ForeignKey('mechanic.id'))
    part_id = Column(Integer, ForeignKey('part.id'))
    amount = Column(Numeric(9,2))
    service_date = Column(Date)
    
    customer_car = relationship('CustomerCar', backref='customer_car')
    mechanic = relationship('Mechanic', backref='mechanic')
    part = relationship('Part', backref='part')

class InventoryCar(Base):
    __tablename__ = "inventory_car"

    serial_number = Column(String(255), primary_key=True)
    price = Column(Numeric(9,2))

class Part(Base):
    __tablename__ = "part"

    id = Column(Integer, primary_key=True)
    part_name = Column(String(255))
    price = Column(Numeric(9,2))

class Record(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))

    invoice = relationship('Invoice', backref='invoice')

class ServiceTicket(Base):
    __tablename__ = "service_ticket"

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey('service.id'))
    
    service = relationship('Service',backref='service')

Session = sessionmaker(db)
create_session = Session()

Base.metadata.create_all(db)

# doctor_strange = Film(title='Doctor Strange',director='Scott Derrickson',year='2016')
# create_session.add(doctor_strange)
# create_session.commit()

# films = create_session.query(Film)

#for film in films:
#    print(film.title)