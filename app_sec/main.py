from flask import Blueprint, render_template
from flask_login import login_user, logout_user, login_required, current_user
from app_sec.models import User, Product
from app_sec.models import AddToWishlistForm, AddToCartForm, AddProductForm
from app_sec import db
from flask import request, redirect, url_for
main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
@login_required
def index():
    wishadd=AddToWishlistForm()
    cartadd=AddToCartForm()
    user=User.query.filter_by(id=current_user.id).first()
    products = Product.query.all()
    return render_template('index.html',user=user, products=products,wishadd=wishadd,cartadd=cartadd)


@main.route('/' , methods=['POST'])
@login_required
def index_post():
    wishadd=AddToWishlistForm()
    cartadd=AddToCartForm()
    products = Product.query.all()
    return render_template('index.html', products=products,wishadd=wishadd,cartadd=cartadd)


@main.route('/product/<int:product_id>', methods=['GET'])
@login_required
def product(product_id):
    wishadd=AddToWishlistForm()
    cartadd=AddToCartForm()
    product = Product.query.filter_by(id=product_id).first()
    if not product:
        return render_template('404.html')
    return render_template('product.html', product=product,wishadd=wishadd,cartadd=cartadd)


@main.route('/addproduct', methods=['GET'])
@login_required
def add_product():
    add=AddProductForm()
    user=User.query.filter_by(id=current_user.id).first()
    if user.isAdmin == False:
        return render_template('404.html')
    else:
        return render_template('addproduct.html',add=add)

@main.route('/addproduct', methods=['POST'])
@login_required
def add_product_post():
    name = request.form.get('name')
    price = request.form.get('price')
    description = request.form.get('description')
    category=request.form.get('category')
    if category == 'Merchandising':
        category_id=1
    elif category == 'Clothing':
        category_id=2
    else:
        category_id=3
    product = Product(name=name, price=price, description=description, category_id=category_id)
    db.session.add(product)
    db.session.commit()
    return redirect(url_for('main.index'))