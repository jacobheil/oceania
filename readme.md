# Practice: Python and Omeka
#### scraping, cleaning, restructuring, reconstituting data for Omeka ingest

This is just a pet project that's an offshoot of the [Mapping Oceania](http://www.mappingoceaniadenison.org/), which was quickly designed by Debbie Andreadis and Christian Faur for a class project for Joanna Grabski's class on _Mapping the Arts of Oceania_. It's not actually affiliated with the project, but I've taken it as a dataset that will allow me to practice batched exporting from PDF, batch metadata editing, conversion to CSV, and upload to Omeka, all using Python. You can see my [process](#process) below, and learn a little more about why I'm doing this [immediately below](#a-little-background). 

### A little background
In the original assignment students located digital images of two examples of Oceanic art and/or artifact and then wrote a short paper contextualizing the relationship between the two. The assignment was conceived as an [Omeka](http://omeka.org/) project because Omeka is really good at metadata and at allowing for the curation of exhibits (precisely what the students are doing here). The desire was to recontextualize these examples of Oceanic Art, the material manifestations of which live all over the globe, using a kind of virtual museum and exhibit space. For simplicity (and to be safe vis-a-vis copyright) the assignment asked students to create these exhibits in Word, transform them to PDF, and then upload the PDFs to Omeka. In essence, the "objects" in the Omeka site were the students' PDF'd assignments. 

In their assignments, and in consultation with the librarian, the students gathered metadata on their projects and included them as part of the assignment. You can [see examples here](http://www.mappingoceaniadenison.org/items/browse?collection=1). It was a good opportunity to teach students about the importance of metadata, but because that metadata is trapped in the PDFs it's utility is limited to exercise of gathering it as such; the Oceanic objects aren't able to be linked with one another outside of the individual student assignments and tags, which were not selected with a controlled vocabulary. Again, this was a compromise becuase of well-placed concerns with copyright infringement.

The result, though, was a dataset of PDFs from which I wanted to extract the images and the metadata first so that I could reconstitute the collection as a large set of digital surrogates for individual artifacts. This give me practice in Python and conversion, but it would also give everyone a clearer sense of how Omeka could be a powerful tool for this project. 

### For the future...
#### or, a note about my stance on copyright here.
[The alpha site](http://www.alpha.mappingoceaniadenison.org/) that I'm making for this collection may not exist for long because I'll reproduce images that were copied by students from other digital archives. This is _probably_ true, even though I'm taking precautions: reproducing them at only 75dpi, I'm linking to the original locations and crediting those locations, and it's the case that the purpose of their re-presentation is the recontextualization that isn't otherwise possible. The pedagogical outcome here is _supposed to be_ that students can see art and artifacts side-by-side and then, by juxtaposing these heretofore unlinked objects, tell stories about Oceanic culture that may not otherwise be available. This, to my mind, is definitionally transformative and, becuase of the low-res images and the direct links _back_ to the source, we're not impeding the parent repo's ability to make a profit. These are the arguments I'd make for fair use here. 

Were I to advise on a project like this again we could do a few things better. (1) Talk about [Creative Commons Licensing](https://creativecommons.org/) and have students only select creative commons images. (2) Work with the parent repositories to negotiate image quality and linking; they may *want* the extra, pedagogically-flavored advertising. (3) Use research or grant funds to purchase some of these images, especially when the parent repo is a small non-profit for indigenous peoples. This project may, in fact, go on to do some of these things, in which case the alpha site may live. But I want to record these lessons here as a part of this code repo as well. 

## Process
1. I exported the XML of the PDF objects from the Oceania Site, and got `oceania.xml`. I used `downloading_pdfs.py`. 
2. I wrote a batch process for Adobe Acrobat Pro 11, pointing it at a directory of PDFs (`/oceania_pdfs/`) and asking it to export as XML.
  * Because the XML was pretty basic it took a lot of transforming and hand-cleaning. The output XML basically wrapped all of the "metadata" that was captured by the students -- indeed everything in the doc, including the students' written parts and the bibliography at the end -- in `<p>` tags. You can see this in [`/oceania_pdfs/_ocr_output_xml`](https://github.com/jacobheil/oceania/tree/master/oceania_pdfs/_ocr_output_xml).
  * There was a large header that wasn't that helpful, so I could just extract the three main sections that I needed: metadata, written part, and bibliography. These ended up in [`/oceania_pdfs/_ocr_output_parsed`](https://github.com/jacobheil/oceania/tree/master/oceania_pdfs/_ocr_output_parsed) and then [`/oceania_pdfs/_ocr_output_structured`](https://github.com/jacobheil/oceania/tree/master/oceania_pdfs/_ocr_output_structured).
  * In the latter of these, "structured," I was able to section off the `<metadata>` sections and then extract those to [`/oceania_pdfs/_oceania_metadata`](https://github.com/jacobheil/oceania/tree/master/oceania_pdfs/_oceania_metadata).
[//]: # (Include links to the scripts in the three substeps above.)
3. In order to be able to upload images to Omeka using CSV (more below) I'd have to have a persistent link to the images. As a test I zipped 20 up, which meant that I was trying to import data from ten of the converted, extracted PDFs (remember that each PDF was a would-be exhibit of two items and attendant metadata each). I unzipped that image dir onto the server with the intention of deleting it as soon as the upload was complete. 
4. From here I started the process of hand-cleaning. This involved:
    * Checking that files were associated with the proper images on the server
    * Closing tags
    * Ordering Metadata and giving item-level structure
5. Used `csv_conversion.py` to convert the glommed metadata into a CSV file
	* I'm using [this tutorial](http://blog.appliedinformaticsinc.com/how-to-parse-and-convert-xml-to-csv-using-python/). My XML was not well-formed: for XML tree to work you have to have a root element that encloses the whole thing. I just used `<items>`.
	* make sure the metadata is right or it'll throw an error. 
6. Using the [CSV Import plugin](https://omeka.org/codex/Plugins/CSV_Import_2.0) I was pretty easily able to import the records from the interwebs. 
	* I was then able to delete the temporary directory that I stashed on the server to hold the edited images, just until they could be uploaded to the site. (I changed the DPI to 75 for all of them.)
	* I ran into an error related to Omeka on hosted services. I used [this from the Reclaim Docs](http://docs.reclaimhosting.com/omeka/working-with-omeka) to solve it.

## Exhibit making from scraped PDFs
1. This required some work by hand, but probably less than if I were just copying and pasting all of these steps from PDFs. 
2. In order to recreate the PDF exhibits ([example here](https://github.com/jacobheil/oceania/blob/master/oceania_pdfs/d827efd96e61a0f2615b6c06ab90f566.pdf)) I created a parent exhibit -- Polynesia and Melanesia -- and then hand-transferred the information from each PDF page into an exhibit "page", [like this one](http://www.alpha.mappingoceaniadenison.org/exhibits/show/melanesia/feast-bowl-admiralty-islands--).
3. hand-copied text in at least three parts
	1. First "file with text" in which I pasted the text alongside one of the two Oceanic objects featured in the PDF exhibit.
	2. Second "file with text" for the other object and the rest of the text.
	3. "Text only" section in which I pasted the bibliograpy. 
4. For the bibliography 
	1. I converted any links to actual HTML links by hand, and 
	2. pasted that into [a web-based HTML converter](http://www.textfixer.com/html/convert-text-html.php) (to save me the steps of keying `<p>` tags and the like).
	3. Finally I opened the [HTML editing window](https://omeka.org/codex/Using_HTML_Editor-TinyMCE), pasted the converted text.
5. REPEAT for each exhibit in the `test_batch`.

## Next Steps
1. Clean data from the remaining 20 PDFs to create 40 new objects and import them. 
2. Import the student reports as exhibits


