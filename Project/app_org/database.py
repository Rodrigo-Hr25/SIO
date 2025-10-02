from flask import Blueprint, jsonify
from app_org import db
from app_org.models import User, Product, Category, Course
from werkzeug.security import generate_password_hash

database = Blueprint('database', __name__)

@database.route('/generate', methods=['GET'])
def create_db():
    db.create_all()
    return jsonify({'message': 'Database created successfully!'}), 200

@database.route('/generate/users', methods=['GET'])
def create_users():
    db.session.execute('DELETE FROM user WHERE isAdmin = False')
    db.session.commit()
    users = [{
        'username': 'user1',
        'email': 'user1@ua.pt',
        'password': generate_password_hash('password1', method='sha256'),
        'first_name': 'user',
        'last_name': 'one',
        'isAdmin': False,
        'phone_number': '123456789',
        'image': 'default.png',
        'address': 'Aveiro',
        'failed_login_attempts': 0,
    }, {
        'username': 'user2',
        'email': 'user2@ua.pt',
        'password': generate_password_hash('password2', method='sha256'),
        'first_name': 'user',
        'isAdmin': False,
        'phone_number': '987654321',
        'image': 'default.png',
        'address': 'Aveiro',
        'failed_login_attempts': 0,
    }, {
        'username': 'lucifer666',
        'email': 'lucifer666@ua.pt',
        'password': generate_password_hash('hell', method='sha256'),
        'first_name': 'Lucifer',
        'isAdmin': True,
        'failed_login_attempts': 0,
    }]
    try:
        db.session.bulk_insert_mappings(User, users)
        db.session.commit()
        return jsonify({'message': 'Users created successfully!'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Error creating users!'})

@database.route('/generate/courses', methods=['GET'])
def create_courses():
    db.session.execute('DELETE FROM course')
    db.session.commit()
    courses = [
        {'name': 'Engenharia de Computadores e Informática'},
        {'name': 'Engenharia Informática'},
        {'name': 'Ciência da Computação'}
    ]
    db.session.bulk_insert_mappings(Course, courses)
    db.session.commit()
    return jsonify({'message': 'Courses created successfully!'})

@database.route('/generate/products', methods=['GET'])
def create_products():
    db.session.execute('DELETE FROM product')
    db.session.commit()
    products = [{
        'name': 'Mug',
        'description': 'Coffee Break',
        'price': 3,
        'image': 'mug.png',
        'category_id': 1,
        'quantity': 10,
        'course_id': 1,
        'has_size': False,
        'has_color': False,
        'size': 'N/A',
        'color': 'N/A'
    }, {
        'name': 'Speaker',
        'description': 'A personalized Deti Speaker',
        'price': 20,
        'image': 'speaker.png',
        'category_id': 1,
        'quantity': 10,
        'course_id': None,
        'has_size': False,
        'has_color': False,
        'size': 'N/A',
        'color': 'N/A'
    }, {
        'name': 'Mousepad',
        'description': 'A personalized Deti Mousepad',
        'price': 5,
        'image': 'mousepad.png',
        'category_id': 1,
        'quantity': 0,
        'course_id': None,
        'has_size': False,
        'has_color': False,
        'size': 'N/A',
        'color': 'N/A'
    }, {
        'name': 'Bag',
        'description': 'A personalized Deti Bag',
        'price': 2,
        'image': 'bag.png',
        'category_id': 1,
        'quantity': 5,
        'course_id': None,
        'has_size': False,
        'has_color': False,
        'size': 'N/A',
        'color': 'N/A'
    }, {
        'name': 'Sweatshirt',
        'description': 'A personalized Deti Sweatshirt',
        'price': 25,
        'image': 'sweat.png',
        'category_id': 2,
        'quantity': 12,
        'course_id': 2,
        'has_size': True,
        'has_color': True,
        'size': 'L',
        'color': 'Preto'
    }, {
        'name': 'T-Shirt',
        'description': 'A personalized Deti T-Shirt',
        'price': 15,
        'image': 'tshirt.png',
        'category_id': 2,
        'quantity': 1,
        'course_id': None,
        'has_size': True,
        'has_color': True,
        'size': 'M',
        'color': 'White'
    }]
    try:
        db.session.bulk_insert_mappings(Product, products)
        db.session.commit()
        return jsonify({'message': 'Products created successfully!'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Error creating products!'})

@database.route('/generate/categories', methods=['GET'])
def create_categories():
    db.session.execute('DELETE FROM category')
    db.session.commit()
    categories = [{
        'category_id': 1,
        'name': 'Merchandising',
    }, {
        'category_id': 2,
        'name': 'Clothing',
    }]
    try:
        db.session.bulk_insert_mappings(Category, categories)
        db.session.commit()
        return jsonify({'message': 'Categories created successfully!'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Error creating categories!'})

@database.route('/generate/all', methods=['GET'])
def create_all():
    create_db()
    create_users()
    create_categories()
    create_products()
    create_courses()
    return jsonify({'message': 'All created successfully!'})