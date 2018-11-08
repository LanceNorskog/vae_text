import json
import sys

# parse caption files from MSCOCO datasets
# group captions by image_id
# allow filtering of single-entry images, we want 2 or more sentences per image

def parse(f):
   
  annotations = json.load(f)['annotations']
  images = {}
  max_len = 0
  for record in annotations:
    if record == None:
      continue
    image_id = record['image_id']
    caption = record['caption']
    if not image_id in images:
      images[image_id] = []
    images[image_id].append(caption)
    if len(images) > max_len:
      max_len = len(images)
  for image_id in images.keys():
      for caption in images[image_id]:
        if caption.startswith('\n'):
          caption = caption[1:]
        if caption.endswith('\n'):
          caption = caption[:-1]
        yield image_id, caption

if __name__ == "__main__":
  for (image_id, caption) in parse(sys.stdin):
    print(str(image_id) + "\t" + caption)
