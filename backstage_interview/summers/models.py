''' Summers Models
'''
# from django.db import models
import datetime

class SummationDifferenceValueError(ValueError):
    ''' N is outside of the range 1 to 100.
    '''

class SummationDifference(object):
    ''' Summation Difference is a strange measure.

    The `value` is the difference between these two summands:
    The sum of the squares of the first n natural numbers 

        sigma(K**2, K=[1, N]) = n(n + 1)(2n + 1)/6

        ...and...

    The square of the sum of the same first n natural numbers:

        sigma(K, K=[1, N]) = n(n + 1)/2

    N must be no greater than 100.
    '''

    def __init__(self, n):
        ''' Create a new SummationDifference and compute its `value`.

        :param int n: a natural number between 1 and 100
        :raises SummationDifferenceValueError: N is outside of the range
        '''
        if (n < 1) or (n > 100):
            raise SummationDifferenceValueError('n=%r is outside of the range [1, 100]' % n)

        self.number = n
        self._occurrences = 0
        self._timestamp = datetime.datetime.now()
        self._set_value()

    @property
    def occurrences(self):
        ''' The counter for many times this number occurred.

        :rtype int:
        '''
	return self._occurrences

    def update(self):
        ''' Update the occurances counter. 
        '''
	self._occurrences += 1
        self._timestamp = datetime.datetime.now()

    @property
    def value(self):
        ''' The counter for many times this number occurred.

        :rtype int:
        '''
	return self._value

    def _set_value(self):
        '''  Compute the `value` and store it as a read-only property.
        ''' 
        value = 0
        k = self.number
        term1 = k*(k + 1)
        term2 = 2*k - 2
        value += term1*term2/6

	self._value = value

    def to_dict(self):
        ''' Represent this object as a dictionary.
        This is suitable to make JSON.
        '''
        return {
            'number': self.number,
	    'value': self._value,
	    'occurrences': self._occurrences,
	    'datetime': self._timestamp,
        }

    def cache_key(self):
        ''' Compute the cache key.
        '''
        return '%s:number=%d' % (self.__class__.__name__, self.number)

