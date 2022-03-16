TROG Task
---------

Due to copyright issues, Stimuli for this task are not distrubuted with MOREDAT. This means that as an admin of a MOREDAT instance, you will have to find them yourself or create custom stimuli.

The original TROG-2 had 20 blocks (A – T) of stimuli, consisting of 4 sets of images (A has 5, one for practice), which targeted different areas of grammar. Each set of images has a corresponding audio prompt and consists of one target image and three distractor images.

As a concrete example. If your block A is about spatial relations, you might have an audio prompt for set A1, where someone reads "The cat is on the table."

A1_1_t.jpg, the target image (t in the file name), depicts a cat on a table. A1_2_d.jpg, A1_3_d.jpg, A1_4_d.jpg, are all distractor images and depict scenarios that don't match the target audio prompt, but may be easily confused by someone who's not proficient in spatial relations in the target language – A cat under the table, behind, or next to the table.

Importantly (!!) 

	– the image stimuli must be named following these conventions and should live at static/trog/img/.

	– the audio prompt should be named with the following convention: {short_language_code}_{image_set}.wav. So eg For the Dothrak group the A1 set audio prompt would be called dot_A1.wav. These files live at static/trog/cues.

	– if you don't follow these conventions, you must update the views.py file as well as the trog templates and javascript (static/trog/trog-trial.js) to reflect the new file naming conventions.