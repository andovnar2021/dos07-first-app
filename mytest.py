from http import client




def test_simple1():
    mylist = [1,3,5]
    
    assert 1 in mylist
    
    
# def test_get():
#     res = client.get('/search4')
#     assert res.status_code == 200

def test_simple2():
    mylist = [1,3,5]
    
    assert 3 in mylist
    
    
def test_simple3():
    mylist = [1,3,5]
    
    assert 5 in mylist