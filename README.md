# Stephens Pop Shop

This is my fourth milestone and ironically my fourth attempt.

As this is my fourth attempt I will include links to my previous attempts that can be found at

- <https://github.com/jjackson19862017/PopWorld>
- <https://github.com/jjackson19862017/popworld2>
- <https://github.com/jjackson19862017/popworld3>

I will be using previous code, from my past attempts to save me time.  As I only have 3 days to complete this project and submit it in for assessment.  I have started again, has I was trying to be clever and do everything in my head.  I realise my tables could be managed and designed better.  I actually went old school and wrote my tables out and drew the links.  Visually seeing it was better for me to understand where I could of gone wrong previously.

## Lets Get Down To Business

For my Fourth and Final Milestone Project have chosen to build a project based on an auction website involving Pop!Vinyl's.  The goal of the website is for the Owner to advertise his Pop!Vinyl collection and sell them to the public involving either bidding for items or buying them out-right.

I will set up an authentication and authorisation.  Where only registered users can bid and buy items that are up for auction.

When the buyers come to purchase their goods, they will be using the Stripe Payment Method.

## Project Brief

- Earn money on selling the toys known as Pop!Vinyl's (the site owner is the seller)

- Create an online store focused on selling Pop!Vinyl's, from different series to the highest bidder.

- Allow users to search for Pop!Vinyl's based on various fields.

- Allow users to see the price, image and other basic details about an Pop!Vinyl.

- Allow users to bid on items, or pay a higher price to purchase them immediately. Users have to be registered for this.

### Advanced potential feature (nice-to-have)

Allow registered users to write reviews about the Pop!Vinyl's, only if they purchased them.

Expand the search functionality to allow users to sort results based on price, character and other parameters in both ascending and descending order.

Include pagination and/or other dynamic display actions using javascript or bootstrap.

Use javascript polling to update the page whenever there's a new bid.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

| Technology      | How it was used                                                 | Website                                            |
| :--------------:|-----------------------------------------------------------------|---------------------------------------------------:|
| HTML            | Backbone of everything                                          | <https://www.w3schools.com/html/default.asp>         |
| CSS             | Styling for the MATERLIZE to work on                            | <https://www.w3schools.com/css/default.asp>          |
| MATERLIZE       | A modern responsive front-end framework based on Material Design| <https://materializecss.com/>                        |
| JAVASCRIPT      | Used for some functionality on the website                      | <https://www.w3schools.com/js/default.asp>           |
| PYTHON          | Used for the main functionality on the website                  | <https://www.w3schools.com/python/default.asp>       |
| SQLITE3         | Light Local Database                                | <https://www.sqlite.org/index.html>       |
| POST GRE           | Non-Relational Database                                         | <https://cloudmongo.com>                             |
| DJANGO          | Web Framework                                                    | <https://www.djangoproject.com/>|
| HEROKU          | Cloud Platform to Host the Django App                            | <https://id.heroku.com/login>                        |
| TRAVIS          | Testing Platform                                                 | <https://www.travis-ci.org/>                        |
| GITHUB          | Stores my work so that other people and myself can reference it | <https://www.github.com>                             |
| GITPOD          | An IDE allowing me to code on any browser                       | <https://www.gitpod.io>                              |
| VSCODE          | An IDE allowing me to code on my computer                       | <https://code.visualstudio.com/>                     |
| SLACK           | An chat application to allow others to communicate              | <https://slack.com/intl/en-gb/>                      |
| Stripe JS       | For easy payment when user select paynow option on all screen sizes | <https://stripe.com/ie>               |

## Places I Have Looked For Help

- Django Documentation - <https://docs.djangoproject.com/en/3.0/>
- Pop In a Box - <https://www.popinabox.co.uk/> - These were used for the Product Images

## Timeline

### Thursday 26th March 2020

Started project for a fourth time, going to commit my readme.md and env.py and gitignore as my --> "Initial Commit".

Time to create my project called "popshop", and change the settings file to hide hidden keys etc.

I will also create the static and media folder structure.

--> "Project Setup"

Create accounts for users.

Created Superuser

--> "Accounts App Created"

Create Products app for Products to populate with.

Created Templates folder as I forgot to do that when I was creating my static folder.

--> "Products App Created"

Create Search app for users to search for potential products.

--> "Search App Created"

Create Cart app for users to buy products.

--> "Cart App Created"

Create Checkout app for users to make payments.

--> "Checkout App Created"

Create Auction app for the owner to create auctions.

--> "Auction App Created"

Create Bids app for the users to bid on auctions.

--> "Bid App Created"

So now I am back to where I started however there are a few adjustments I have to make due to the fields changing tables.

Also got rid of home redirect as I am not using a home app this time around.

--> "Field Updates"

While building and testing my website, I have found it annoying to remember who I am logged in as, so I have modified the base.html to run an if statement to see if I am a superuser.  If that is true then the navbar will turn Red.

I have also moved around the links on the navbar.

--> "Navbar Update"

I thought it would be some nice feedback for the user, if the loops were empty.  Ie no products or auctions.  I found the solution on <https://docs.djangoproject.com/en/1.11/ref/templates/builtins/>

I also changed the way the cart and checkout looks, they now appear as tables so it looks like an invoice.

--> "Empty Lists UI Update"

I have found a problem with paying for things with Stripe so I am watching the videos again.

My jquery and the stripe js was being loaded out of order.

--> "Fixed Stripe Payments"

I have changed everything from Pop World to Pop Shop.

I have also hidden the cart if it is empty.  This is to stop people from openning an empty cart.

--> "Shop Update"

I have got the bids to work with the new field in the other table

--> "Bids Working"

Safe this for later

            {% if i.user_id.username != user.username %}
            <form action="{% url 'bid_on_auction' %}" method="POST">
                {% csrf_token %}
                <div class="input-group">
                    <input type="hidden" name="product_id" value={{ auction.product_id.id }} />
                    <input name="UpBid" type="number" min="5" max="9999" class="form-control" placeholder="Enter minimum £ 5">
                    <span class="input-group-btn"><button class="btn btn-success">Increase Bid</button></span>
                </div>
            </form>
          {%else%}
            <p class="product-text text-center">You cannot bid again, <br>Wait till someone else bids.</p>
            {%endif%}

### Saturday 28th March 2020

I tried to see if I could display my bid data on my auction site, however after many tries.  I created a field in the auction model that is updated by the open_auction

--> "Auction Models Updated"

Updated some links, and changed the base.html to reflect open and closed auctions.

Researched Countdown Timers for JS <https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_countdown>

Unfortunately can't get it to work at the present time, will focus on the task I have been putting off and thats getting my winning bid to purchase.

Im so close to getting it working, just need some help.

--> "Nearly there with putting a winning bid into a cart"

I have spent nearly 2 hours looking on how to put this PRICE from add_to_cart view into the cart_contents context

def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))
    price = float(request.POST.get('price'))
    print("id: " + str(id))
    print("price: " + str(price))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity  
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

  def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        
        price = product.instant_buy_price

        total += quantity * price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
        print("product: "+str(product))
        print("total: "+str(total))
        print("product count: "+str(product_count))
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}

Thank you Anne and Tim about sessions, I have got further now

--> "Session Price"