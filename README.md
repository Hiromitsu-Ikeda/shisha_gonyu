# shisha_gonyu

This packeage can round off a value or an array-like object.

## Installation
1. Clone this repositry.
2. Move the "shisha_gonyu" directory into the "site-packages" directory in your python environment.

## Usage

### Decimal
Set the argument "decimal_bool" to True. (Default)
#### Example
If 108.88 is rounded off to the first decimal place, it becomes 108.9.
1. input as a str object and return as a str object


```python
import shisha_gonyu
value = '108.88'
shisha_gonyu.shisha_gonyu(value=value,digit=1,type_=str,decimal_bool=True)
```




    '108.9'



2. input as a str object and return as a float object


```python
import shisha_gonyu
value = '108.88'
shisha_gonyu.shisha_gonyu(value=value,digit=1,type_=float,decimal_bool=True)
```




    108.9



3. input as an array object and return as an numpy.ndarray object of which type is float


```python
import shisha_gonyu
value = [108.88]
shisha_gonyu.shisha_gonyu(value=value,digit=1,type_=float,decimal_bool=True)
```




    array([108.9])



### Integer
Set the argument "decimal_bool" to False.
#### Example
If 108 is rounded off at the ones digit, it becomes 110.
1. input as a str object and return as a str object


```python
import shisha_gonyu
value = '108'
shisha_gonyu.shisha_gonyu(value,digit=1,type_=str,decimal_bool=False)
```




    110



2. input as a float object and return as a float object


```python
import shisha_gonyu
value = 108
shisha_gonyu.shisha_gonyu(value,digit=1,type_=float,decimal_bool=False)
```




    110



3. input as an array object and return as an numpy.ndarray object of which type is float


```python
import shisha_gonyu
value = [108.88]
shisha_gonyu.shisha_gonyu(value,digit=1,type_=float,decimal_bool=False)
```




    array([110.])


