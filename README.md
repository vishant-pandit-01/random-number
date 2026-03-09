# Python Random Module Examples

This repository contains simple examples of using Python's **random module** to generate random numbers and select random values from a list.

## 📌 Features

* Generate a random number in a range
* Select a random value from given data
* Random color selection
* Select multiple random samples from a list

## 🧾 Code Example

```python
import random

# ----- for random digit -----
x = random.randrange(1,1000)
print(x)

# ----- for random value in given data -----
print(random.choice(['A','B','C','D','E']))

# ----- for random color -----
print(random.choice(['red','green','yellow']))

# ----- for multiple samples -----
print(random.sample(['1','2','3','4','5','6'],3))
```

## ⚙️ Functions Used

### 1. `random.randrange(start, stop)`

Generates a random number within the given range.

Example:

```
random.randrange(1,1000)
```

### 2. `random.choice(sequence)`

Returns a random element from a list or sequence.

Example:

```
random.choice(['A','B','C','D','E'])
```

### 3. `random.sample(sequence, k)`

Returns **k unique random elements** from a list.

Example:

```
random.sample(['1','2','3','4','5','6'],3)
```

## ▶️ How to Run
