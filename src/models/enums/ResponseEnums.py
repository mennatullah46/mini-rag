from enum import Enum

class ResponseSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = "File Type not Supported"
    FILE_SIZE_EXCEEDED = "File Size Exceeded"
    FILE_UPLOADED_SUCCESSFULLY = "File Uploaded Successfully"
    FILE_UPLOAD_FAIL = "File Upload Failed"
    PROCESSING_FAILED = "Processing Failed"
    PROCESSING_SUCCEEDED = "processing Succeeded"
    NO_FILES_ERROR = "Files not found"
    FILE_ID_ERROR = "no_file_found_with_this_id"
    PROJECT_NOT_FOUND_ERROR = "project_not_found"
    INSERT_INTO_VECTORDB_ERROR = "insert_into_vectordb_error"
    INSERT_INTO_VECTORDB_SUCCESS = "insert_into_vectordb_success"
    VECTORDB_COLLECTION_RETRIEVED = "vectordb_collection_retrieved"
    VECTORDB_SEARCH_ERROR = "vectordb_search_error"
    VECTORDB_SEARCH_SUCCESS = "vectordb_search_success"