# Instructions Parser
## Background
You are working for a manufacturing company and are trying to make your product as cheaply as
possible. Let's say you're making teddy bears. You can potentially buy painted glass eyeballs, tiny
shirts, fake bear cloth, and sewing thread, and put them all together in your factory to produce the
teddy bear. But to save money, maybe you can build the painted glass eyeballs yourself by buying
glass and paint. And so on and so forth. You could even build your own paint if it's cheaper than
purchasing paint directly! This program figures out the cheapest way to make your product. There
are no costs associated with combining inputs into a product. The first part of the input is the
product you are trying to obtain (the "target product"). The second part is data representing how
to build and/or purchase various products. Finally the program writes to stdout the cheapest way to obtain the
target product (either via building it yourself or purchasing it).

## Input Description
 - A target product ( target_product )
 - For each Product:
   - The name of the product ( product_name )
   - The price to purchase the product directly ( price_to_purchase )
   - The number of materials required as inputs to build the product ( input_products_size )
   - A list of materials required as inputs to build the product ( input_products )
     
If price_to_purchase is null , it is impossible to purchase that product. If input_products is
empty, it is impossible to build that product
These inputs will be formatted like this:
<target_product>
<product_name>,<price_to_purchase>,<input_products_size>,<input_products>
<product_name>,<price_to_purchase>,<input_products_size>,<input_products>
<product_name>,<price_to_purchase>,<input_products_size>,<input_products>
<product_name>,<price_to_purchase>,<input_products_size>,<input_products>

## Example
teddy bear
painted glass eyeball,10.5,2,glass;paint
glass,5,0,
paint,4,0,
teddy bear,null,4,painted glass eyeball;tiny shirt;faux bear fur fabric;sewin
g thread
faux bear fur fabric,15,2,bear;yarn
bear,100,0,
yarn,2,0,
sewing thread,13,0,
tiny shirt,24,0,

In the above example, we are making teddy bears, since that is in the first row of the input. Teddy
bears are not able to be purchased on the market ("null" in the second column of the input), thus
you'll have to build the teddy bear yourself.

It is cheaper to build the "painted glass eyeball" yourself out of glass and paint, instead of purchasing
the eyeballs ($5 + $4 < $10.5). However, it is cheaper to purchase the "faux bear fur fabric", rather
than make it yourself out of bear and yarn ($15 < $100 + $2). Since the list of inputs is empty for
sewing threads and tiny shirts, that means they must be purchased for $13 and $24, respectively. So
the cheapest price to produce teddy bears would be calculated below:

5 (glass)

4 (paint)

15 (faux bear fur fabric)

24 (tiny shirt)

13 (sewing thread)

$61

To format this properly, you should write 61.00 to stdout.

## Running the test suite
To run the code, simply clone the repo and run ```./run_tests.sh```
