def getAttachmentBasePath():
    return "/home/jmmans/tmp/ePortage"
#    return "/home/daq/ePortageArchive/uHTR"

def getAttachmentPathFor(test_id,attach_id):
    return "%s/%d/%d" % (getAttachmentBasePath(),test_id,attach_id)
