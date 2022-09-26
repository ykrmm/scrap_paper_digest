# Scrap Paper Digest Highlights conf 

## Step 1: Go to [Conference Paper Digests by Year](https://www.paperdigest.org/conference-paper-digest/)

Select the url of the conference you want scrap.
Example ICML 2022 Conference : https://www.paperdigest.org/2022/07/icml-2022-highlights/


## Step 2 : Run the program scrapper with your key word 

Search the key words 'graph' AND 'dynamic' only in the title

`python scrap_paper_digest.py --url https://www.paperdigest.org/2022/04/www-2022-highlights/ -w graph dynamic --all > dynamic.txt`

Search the key words 'graph' OR 'dynamic' only in the title

`python scrap_paper_digest.py --url https://www.paperdigest.org/2022/04/www-2022-highlights/ -w graph dynamic > dynamic.txt`

Search the key words 'graph' OR 'dynamic' in the title AND in  the highlights 

`python scrap_paper_digest.py --url https://www.paperdigest.org/2022/04/www-2022-highlights/ -w graph dynamic --search_highlights > dynamic.txt`
