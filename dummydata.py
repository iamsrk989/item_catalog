from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, ProductItem, User

engine = create_engine('sqlite:///categoryproductwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Sridhar", email="sridhar69friends@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Product for Mobile and Tablets
category1 = Category(user_id=1, name="Mobile and Tablets")

session.add(category1)
session.commit()

productItem2 = ProductItem(user_id=1, name="Apple iPhone 7", 
                           description=" iPhone with iOS 10, EarPods with Lightning Connector",
                           price="$750", category=category1)

session.add(productItem2)
session.commit()


productItem1 = ProductItem(user_id=1, name="Samsung galaxy s8", 
                           description="S8+ is latest smartphone with IRIS Scanner, 12 MP Dual Pixel camera and more",
                           price="$799", category=category1)

session.add(productItem1)
session.commit()

productItem2 = ProductItem(user_id=1, name="One Plus 3T", 
                           description="Never Settle",
                           price="$550", category=category1)

session.add(productItem2)
session.commit()



# Product for Laptops and PCs
category2 = Category(user_id=1, name="Laptops and PCs")

session.add(category2)
session.commit()


productItem1 = ProductItem(user_id=1, name="Hp Pavillion Notebook", 
                           description="Awesome Laptop at affordable price",
                           price="$799", category=category2)

session.add(productItem1)
session.commit()

productItem2 = ProductItem(user_id=1, name="Dell Inspiron",
                           description=" Most Durable Laptop", 
                           price="$725", category=category2)

session.add(productItem2)
session.commit()

productItem3 = ProductItem(user_id=1, name="Sony Vaio", 
                           description="Powerful Laptopn with latest processor ",
                           price="$850", category=category2)

session.add(productItem3)
session.commit()

productItem4 = ProductItem(user_id=1, name="Mac Book Air", 
                           description="Elegant Laptop for everyday use ",
                           price="$1000", category=category2)

session.add(productItem4)
session.commit()

productItem5 = ProductItem(user_id=1, name="Alienware Desktop", 
                           description="Hign end PC for Gamers.",
                           price="$1400", category=category2)

session.add(productItem5)
session.commit()

productItem6 = ProductItem(user_id=1, name="HP Desktop", 
                           description="Affordable PC for Day to day use.",
                           price="$500", category=category2)

session.add(productItem6)
session.commit()


print "added product items!"