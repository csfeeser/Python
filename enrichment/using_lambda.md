Below is an example of a typical function. `tenadder` takes an argument (`a`) and adds 10 to it.

```python
def tenadder(a):
    return a + 10

print(tenadder(5))
```

Now, here is the same function written as a **lambda function.**

```python
new = lambda a : a + 10
#1      2    3   ---4---  

print(x(5))
```
- 1. `new` saves the lambda expression so it can be used later.
- 2. all lambda expressions start with the word *lambda*
- 3. `a` is the variable being passed into the function
- 4. The value of `a + 10` is what will be returned from this function.

Here is a normal Python function that uses multiple arguments:

```python
def varadder(a,b):
    return a + b

print(varadder(4,8))
```

Lambda functions can also be passed multiple arguments. Here is the equivalent of the function above written using lambda.

```python
x = lambda a, b : a + b

print(x(4, 8))
```

### TRUE USE OF LAMDAS

The examples above show the anatomy of how a lambda expression works, but doesn't convey how lambda is typically used. In the example below, we'll see how a "vanilla" function (one that's pretty generic and open-ended) can be made to do **more specific** actions using lambda.

```python
def var_exponent(b):
    return lambda a: a ** b
```

Notice the value of `a` has not been provided. That will come later.

```
var_squarer= var_exponent(2)
var_cuber= var_exponent(3)

# WHAT THOSE LINES ABOVE BASICALLY EQUATE TO:
# var_squarer= lambda a: a ** 2
# var_cuber= lambda a: a ** 3
```

`var_squarer` and `var_cuber` take the `var_exponent` function and provide a value for the `a` variable.

```python
#var_squarer returns 5 ^2
print(var_squarer(5))

# var_squarer returns 5 ^3
print(var_cuber(5))
```
