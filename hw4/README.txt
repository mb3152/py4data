Hey Adam! 

I put everything in a notebook with lots of comments so it should be easy to grade.
I put the requested results.txt file in the repo. Although, my accuracy is at the bottom, since I couldn't get it to compute right. I guess I could have hardcoded it in there but that felt wrong. 

You must download the 50_categories and validation_image file to make the file run, since I make a few other objects from those.

Just run through the notebook(only about 10 shift+enters, computations take about 30 second total). This will load the feature array I made instead of making a new one(although you are free to make a new one if you want!). I have a line in there that will pickle the new classifier, and then my function to test new images loads that pickle. There are a few defensive statements in there with comments about what might be wrong if they error. Everything should run as is, but there are lots of comments ensuring names of the pickle and what not are correct. 

Just to be clear, I couldn't get my pickled classifer to be small enough so you will have to make it again in then notebook, but it shouldn't take more than 15 seconds (the whole notebook takes 30).

Also, i need to 50 categories folder in there to make my category names. It fit so i put it in there, plus if i share the repo with people they can walk all the way through it if they want.

My classifier should save out a text file and also print the results. 

One important thing: my classifier takes in images from one flat directory with no subdirectory, and it assumes that the name of the image is the name of category of the image. 

Finally, at the end of the notebook I ran a few tests on images in the test set(just to make sure my function worked) and then random images of bassett hounds from the internet, which did not work at all, except that all the guesses were living animals! 

 a) CV score: 0.31057717266614754
 b) How much better this is than random guessing. Random guessing is .02, so better, but not perfect. Also, 0.1 is the number we get if we just mix up the categories and see how it does. We are still better than this.
 c) 3 most important features: Shape of the image, the number of continuous regions, and the number of edges found by an edge detector. 


0: std of the r_channel
1: std of the g_channel 
2: std of the b_channel
3: mean of the r_channel
4: mean of the g_channel 
5: mean of the b_channel
6: shape of the first dimension of the image array
7: shape of the second dimension of the image array 
8: correlation coefficient of r by g
9: correlation coefficient of r by b
10: correlation coefficient of b by g
11: proportion of all pixels in the image that are part of a vertical edge
12: proportion of all pixels in the image that are part of a horizontal edge
13: number of objects found by segmentation
14: size of the largest object, as a proportion of the total image.
15: number of daisy descriptors
16: number of countours founds
17: number of local maxima 
18: image noise values 
19: image constant values 
20: number of continuous regions
21: number of edges found by edge detector 
