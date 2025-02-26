from app import app
from models import db, User, Service, Park, Hotel, Beach, Favorite

# Create the seed data function
def seed_data():
    # Drop existing data and recreate the tables
    db.drop_all()
    db.create_all()

    # Create users
    user1 = User(
        name="John Doe",
        email="john@example.com",
        phone_number="1234567890",
        password="hashed_password"  
    )
    user2 = User(
        name="Jane Smith",
        email="jane@example.com",
        phone_number="0987654321",
        password="hashed_password"
    )

    # Add Services
    service1 = Service(
        service_name="Kayaking",
        image="https://tinyurl.com/4y2mfxy7", 
        description="Enjoy a thrilling kayaking experience.",
        location="Lake Victoria",
        user_id=user1.id
    )
    service2 = Service(
        service_name="Safari Tour",
        image="https://tinyurl.com/5thzdc64",
        description="Experience a breathtaking safari tour.",
        location="Masai Mara",
        user_id=user2.id
    )

    # Add Parks
    park1 = Park(
        name="Serengeti National Park",
        image="https://tinyurl.com/mvzybp6s",
        description="A majestic wildlife park filled with rich biodiversity.",
        location="Tanzania",
        rating=5,
        address="Serengeti, TZ"
    )
    park2 = Park(
        name="Yellowstone National Park",
        image="https://tinyurl.com/2vn86sve",
        description="Explore the geothermal wonders of Yellowstone.",
        location="USA",
        rating=4,
        address="Yellowstone, WY"
    )
    park3 = Park(
        name="Kruger National Park",
        image="https://tinyurl.com/5c3mr6t8",
        description="Experience the thrill of African wildlife in Kruger.",
        location="South Africa",
        rating=5,
        address="Kruger, SA"
    )
    park4 = Park(
        name="Zion National Park",
        image="https://tinyurl.com/9xv65mxk",
        description="Discover the natural beauty of Zion.",
        location="USA",
        rating=4,
        address="Zion, UT"
    )
    park5 = Park(
        name="Yosemite National Park",
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRU3THzfjyPIUzdjFlf3rWnir3SEMDSKns1Qw&s",
        description="Marvel at the stunning landscapes of Yosemite.",
        location="USA",
        rating=5,
        address="Yosemite, CA"
    )

    # Add Hotels
    hotel1 = Hotel(
        name="Luxury Safari Lodge",
        image="https://tinyurl.com/ysurwsee",
        description="A luxury lodge in the heart of the wilderness.",
        location="Masai Mara",
        rating=5,
        address="Masai Mara, Kenya",
        price_range=300,
        user_id=user1.id
    )
    hotel2 = Hotel(
        name="Coastal Beach Resort",
        image="https://tinyurl.com/6fbay9we",
        description="A resort with stunning views of the ocean.",
        location="Diani Beach",
        rating=4,
        address="Diani Beach, Kenya",
        price_range=250,
        user_id=user2.id
    )
    hotel3 = Hotel(
        name="Mountain Chalet",
        image="https://tinyurl.com/ywnpefxy",
        description="A cozy chalet in the mountains.",
        location="Mount Kenya",
        rating=4,
        address="Mount Kenya, Kenya",
        price_range=200,
        user_id=user2.id
        )
    
    hotel4 = Hotel(
        name="Mercure hotel",
        image="https://tinyurl.com/y3w57nn4",
        description="A lodge with stunning views of the Grand Canyon.",
        location="Grand Canyon",
        rating=5,
        address="Grand Canyon, AZ",
        price_range=400,
        user_id=user2.id
        )

    # Add Beaches
    beach1 = Beach(
        name="Diani Beach",
        image="https://tinyurl.com/23x3amj9",
        description="A pristine white-sand beach on the Kenyan coast.",
        location="Kenya",
        rating=5,
        address="Diani Beach, Kenya"
    )
    beach2 = Beach(
        name="Bondi Beach",
        image="https://tinyurl.com/4yptem6k",
        description="Australia’s iconic beach destination.",
        location="Australia",
        rating=4,
        address="Bondi, NSW"
    )
    beach3 = Beach(
        name="Waikiki Beach",
        image="https://tinyurl.com/ydhdteyy",
        description="A world-famous beach in Honolulu, Hawaii.",
        location="Hawaii",
        rating=5,
        address="Waikiki, HI"
    )
    beach4 = Beach(
        name="Cancun Beach",
        image="https://tinyurl.com/56shkvd4",
        description="A tropical paradise in Mexico.",
        location="Mexico",
        rating=4,
        address="Cancun, Mexico"
    )
    

    # Add Favorites
    favorite1 = Favorite(name="Wildlife Experiences")
    favorite2 = Favorite(name="Beach Getaways")

    # Associate Parks, Hotels, and Beaches with Favorites
    favorite1.parks.extend([park1, park2])
    favorite2.beaches.append(beach1)
    favorite2.hotels.append(hotel2)

    # Commit the objects to the session
    db.session.add_all([user1, user2, service1, service2, park1, park2, park3, park4, park5, hotel1, hotel2, hotel3, hotel4, beach1, beach2, beach3, beach4, favorite1, favorite2])
    db.session.commit()

# Ensure the app context is set up for database operations
if __name__ == '__main__':
    with app.app_context():
        seed_data()
        print("Database seeded successfully!")
