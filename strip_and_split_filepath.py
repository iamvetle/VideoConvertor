def strip_and_split_filepath (filepath: str) -> tuple[str, str]: 
    """
    Strips the strips the full filepath down to just the filename and filetype
    
    Args:
        The filepath as a string
    
    Returns the filename and filetype
    
    """
    
    print("trying to strip and split filepath")
    print(filepath)
    
    try:
        filename = (filepath.split(".")[-2]).split("\\")[0].lower()        
        
        print("filename", filename)
        filetype = filepath.split(".")[-1].lower()
        print("filetype", filetype)
        
        return (filename, filetype)
    except Exception as e:
        print("Something went wrong. Did not manage to strip and split the input:", e)
        exit()
    
    