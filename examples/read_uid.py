from mfrc522 import SimpleMFRC522

if __name__ == '__main__':

    rdr = SimpleMFRC522()
    try:
        uuid = rdr.read_id()
        print(uuid)
        
    except KeyboardInterrupt:
        pass

    finally:
        rdr.READER.close()
