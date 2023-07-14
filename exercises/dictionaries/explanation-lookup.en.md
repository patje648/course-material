# Lookup

In the previous explanation, you were shown how to define a new `dict`:

:::code{caption="Python"}

```python
translating_dictionary = {'cat': 'kat', 'dog': 'hond'}
```

:::

We now turn our attention to actually making use of this `dict`.
The most common operation is to *look up* a value, given a key.

For example, say we want the translation of `cat`.
Here, `cat` is the key, and `kat` is the value we wish to look up in our dictionary.
We can do this as follows:

:::code{caption="Python"}

```python
translation = translating_dictionary['cat']
```

:::

Now, `translation` is equal to `kat`.