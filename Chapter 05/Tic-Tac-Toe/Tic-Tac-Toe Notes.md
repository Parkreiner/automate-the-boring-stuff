# Notes on Tic-Tac-Toe

I'll be using this notation to denote the tic-tac-toe board, with each digit corresponding to a space:

```txt
123
456
789
```

## Checking for a 3-in-a-row

Checking for a 3-in-a-row is pretty easy, as there are only 8 of them in the entire game.

### Possible Winning Patterns

Spaces that are part of the winning lines are marked with an `O`, while all other spaces are marked with an `X`.

#### Vertical Combinations

```txt
OXX   XOX   XXO
OXX   XOX   XXO
OXX   XOX   XXO
```

#### Horizontal Combinations

```txt
OOO   XXX   XXX
XXX   OOO   XXX
XXX   XXX   OOO
```

#### Diagonal Combinations

```txt
OXX   XXO
XOX   XOX
XXO   OXX
```

### "Dumb" Pseudocode for checking win states

#### The checks for [1]

If [1] == [2] and [2] == [3]:
    Win
Elif [1] == [4] and [4] == [7]:
    Win
Elif [1] == [5] and [5] == [9]:
    Win

#### The checks for [2]
If [2] == [5] and [5] == [8]:
    Win

#### The checks for [3]

If [3] == [6] and [6] == [9]:
    Win
Elif [3] == [5] and [5] == [7]:
    Win

#### The checks for [4]

If [4] == [5] and [5] == [6]:
    Win

#### The checks for [7]

If [7] == [8] and [8] == [9]:
    Win

### The patterns from the above

For any space, there are only four possible methods for getting to a space that could be part of a 3-in-a-row with it:

1. Increment by 1 (used to check all horizontals)
2. Increment by 2 (used to check top-right to bottom-left diagonal)
3. Increment by 3 (used to check all verticals)
4. Increment by 4 (used to check top-left to bottom-right diagonal)

Of course, they only work for certain spaces.

1. (1) only is only valid for [1], [4], and [7].
2. (2) is only valid for [3]
3. (3) is only valid for [1], [2], and [3]
4. (4) is only valid for [1]

Although this does mean that I don't have to bother checking from spaces [5], [6], [8], or [9].

[5] - Center
[6] - Middle-Right
[8] - Bottom-Middle
[9] - Bottom-Right

#### Spaces to check

```txt
OOO     O - Check
OXX     X - Don't need to check
OXX
```

So basically, I only need to check a space if one of its values is either "top" or "left". Extending this further:

1. Method (1) is for "left" spaces
2. Method (2) is for the "top-right" space
3. Method (3) is for "top" spaces
4. Method (4) is for the "top-left" space

## Checking for whether a player can still win

Now, this method isn't perfect. It assumes that at least one player won't always make the most optimal move (which is
possible if they have a brain fart and place their symbol in the wrong space). Still, I think the basic idea will work.

I used to think that the best way to check for whether a board was still winnable was by checking the empty spaces, but
now, I actually think the method for checking isn't that different from the method for checking a winning state. When
all is said and done, I might actually be able to combine them.

### What makes a board unwinnable?

A board is definitely unwinnable when none of the eight possible three-in-a-rows can be filled entirely with a single
player's mark. That is, it is unwinnable when it has eight dead ends.

However, a board is also unwinnable when there are seven dead ends and only two empty spaces left. I'm still
experimenting to see if having seven dead ends implies that there are two empty spaces left*. If so, then I can just
mark a game unwinnable when there are seven dead ends.

\* It takes a surprising amount of turns to make a board truly unwinnable when neither player is trying to win.

#### Example of definite unwinnable

```txt
OOX
XXO
OXO
```

#### Example of early unwinnable

```txt
OXO
•X•
XOX
```

### What makes a three-in-a-row a dead end?

A three-in-a-row becomes a dead end when both players have at least one mark inside it.

```txt

START OF TURN 3:

•OX   •: Empty space
•••   X: Player 1
•••   O: Player 2
```

In this example, the horizontal three-in-a-row can no longer be used to win, even though the game has barely started.
Placing an `X` in that remaining empty space doesn't make that row any less unwinnable, but it helps player 1 possibly
win by getting either a vertical or a upper-left-to-bottom-right diagonal.

```txt

START OF TURN 4:

XOX   •: Empty space
•••   X: Player 1
•••   O: Player 2
```

### Extrapolating the "seven dead ends and two empty spaces" case

So, I'm pretty sure that a board is unwinnable when it has seven dead ends and two spaces left. I'm extrapolating that
and seeing if any of these hold up:

1. Is it possible to have seven dead ends and one space left?
2. Is it possible to have seven dead ends and three or more spaces left?
3. Is it possible to have two spaces and less than seven dead ends?
4. Is it possible to have eight dead ends and still have any number of spaces?
5. Is it possible to have seven dead ends and two spaces and still have a winnable board?

The answers:

1. No
2. Yes
3. Yes
4. Yes
5. I don't think so?

#### Addressing 1

From my tests, it seems that if you have one space left and a board that's still winnable (as in, doesn't have eight
dead ends), you'll always have fewer than seven dead ends. That is, having just one space left means that you'll always
have less than seven dead ends.

In this example, there are only five:

```txt
OO•
OXX
XOX
```

And in this example, there are only six:

```txt
XOX
O•O
XXO
```

In both cases, Player 1 wins by placing a `O` in the only blank space. It's impossible for player 2 to win, just because
they get one fewer moves, even though they still have lines that don't contain any `O` marks.

#### Addressing 2

I know that it's possible to have three spaces and seven dead ends:

```txt
O•X
X•O
O•X
```

The only thing is that I don't know if it's possible to have more spaces. I don't think so, though.

### Addressing 3

It is possible to have two spaces left and six dead ends:

```txt
OOX
X•O
•OX
```

The center vertical and the upper-right to lower-left are still open.

### Addressing 4

It is possible:

```txt
OXX
XOO
•OX
```

Even though there's an empty space left, there are already eight dead ends.

### So what am I actually checking for in the code?

I think these are the only scenarios I need to check for:

1. Whether there are eight dead ends
2. Whether there are seven dead ends and two spaces left

So, I think I can just do things like this:

1. Run through the entire board, checking for dead ends
2. Each time I encounter a space, increment counter A by 1
3. Each time I encounter a dead end, increment counter B by 1

If counter B equals 8 or if counter B equals 8 and counter A equals 2, then the game is no longer winnable.