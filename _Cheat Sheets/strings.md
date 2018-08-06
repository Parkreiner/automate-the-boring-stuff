# Strings

## Structure

Strings in Python behave very similarly to lists. However, whereas Python lists are mutable, the same cannot be said of
strings. This is why it's often a bad idea to keep adding to a string before printing it; each time you concatenate to
a string, you're creating a brand new one and throwing the old one out. That's incredibly wasteful for resources.