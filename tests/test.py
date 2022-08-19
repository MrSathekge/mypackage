import imp
from mypackage import myModule

def test_top_n():       # we dont specify ac=rguments, this is just testing the function that we created already
    """
    make sure top_n works perfectly
    """
    

    # assert is how we create a test function.
    # We give it a few test cases, and the answer
    # And we make sure it gives the correct output, they should come out as NOT incorrect

    # THIS IS UNIT TESTING
    assert myModule.top_n([8,3,2,7,4], 3) == [8,7,4], 'incorrect'    #if it's not 8,7,4.. it will type incorrect
    assert myModule.top_n([10,1,12,9,2], 2) == [12,10], 'incorrect'
    assert myModule.top_n([1,2,3,4,5], 5) == [5,4,3,2,1], 'incorrect'







## Now we go to root folder and create 2 more additional files: setup.py, and readme.MD... Then we 1st work on setup