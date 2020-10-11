# PurchasePrediction
This is for the KnightHacks Hackathon. A Heuristic Client that will analyze patterns in purchase behavior and relay that information to the customer as well as predict their purchase habits in the future.


## Purchase History Analysis


**Method 1**: CAT-Fourier Analysis *(Selected Approach)* *

> Let x(t,u) = 0,1 (with fixed constant u in [0,1]) represent whether or not a product was purchased on day t. Then, one can construct an approximate periodic representation x' of x in the CAT-sequence frequency domain. To find the CAT coefficients, solve for the coefficients yk in (4.3.3) or (4.3.6) as a system of linear equations [1].

[1] pp 48-49. https://vtechworks.lib.vt.edu/bitstream/handle/10919/38566/LD5655.V856_1994.L437.pdf?sequence=1&isAllowed=y

-----

Method 2: AI-assisted CAT-Fourier Analysis *

> Same idea as (Method 1), however, the CAT coefficients are approximated using a supervised neural network. Depending on the cost function used during training, the network may compute coefficients that avoid overfitting input data and thus better generalize.

-----

Method 3: Cumulative Price Prediction *

> Instead of predicting the exact days in which a product will be purchased, this method predicts the periodic total cost for a given product purchase history. Similar to (Method 2), the rate is approximated using a supervised neural network. To avoid consideration of price, a multiple of the price may be the output of this network. This may prove more accurate than the other methods since it works on averages rather than minute detail.


* Potentially fixed input size.
