# Fonts

## Font files

## Name-Maps

A mapping from the glyph name to the number or pronunciation of letter the glyph is representing in available in `<FontName>_namesMap.csv`. it is used to have the same id for same glyphs of each font. later extracted glyphs are renamed using this mapping.

#### e.g.

letter `ج` in `traffic_bold` font is named as `u062C`, the name mapping provides would be `JIM`, also number `۲` which is named `two` will be `2`.

> if you want to use another font, name it in snake_case then create the `namesMap.csv` file with the same structure as others and name it `<FontName>_namesMap.csv`.