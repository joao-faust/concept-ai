# Concept AI

Describe concepts and save them in text files with Google's artificial intelligence (Gemini).

Run the command below to get the concepts:
```bash
python main.py --lang=pt-br --input=./input.txt --output=./output.txt
```

Example of input file:

```
PHP
MVC
Laravel
MySQL
```

Example of output file:

```
PHP => About PHP
MVC => About MVC
Laravel => About Laravel
MySQL => About MySQL


```

>Note: It's important to keep the two last lines in blank in order to the script be able to add new lines correctly.
