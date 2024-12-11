# Content Analysis API

A RESTful API to assist content managers in analyzing user feedback and summarizing long documents. This API helps content managers process extensive user feedback and articles efficiently by providing sentiment analysis and text summarization capabilities.

## Features

- **Sentiment Analysis**: Determine the emotional tone of user feedback
- **Text Summarization**: Extract main points from lengthy documents
- **RESTful Architecture**: Simple HTTP endpoints for easy integration

## API Endpoints

### Sentiment Analysis

Analyzes the emotional tone of a given text.

**Endpoint**: `POST /sentiment`

**Request**:
```
{
"text": "I absolutely love this product! The features are amazing and the customer service is outstanding."
}
```
**Response**:

```
{
"text": "I absolutely love this product! The features are amazing and the customer service is outstanding.",
"emotion": "joy",
"confidence": 0.9876
}
```

### Text Summarization

Generates a concise summary of a longer text.

**Endpoint**: `POST /summarize`

**Request**:
```
{
"text": "New York (CNN) When Liana Barrientos was 23 years old, she got married in Westchester County, New York. A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband. Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared 'I do' five more times, sometimes only within two weeks of each other. In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her 'first and only' marriage. Barrientos, now 39, is facing two criminal counts of 'offering a false instrument for filing in the first degree,' referring to her false statements on the 2010 marriage license application, according to court documents."
}
```
**Response**:

```
{
"summary": "Liana Barrientos married multiple times without divorcing previous husbands.",
"original_length": 432,
"summary_length": 71
}
```

## Error Responses

### Bad Request (400)
```
{
"detail": "Text is required"
}
```
### Internal Server Error (500)
```
{
"detail": "Internal Server Error: [error message]"
}
```


## Installation and Running

Execute `bash setup.sh` for installation and running the server on port 8000.
Command: `bash setup.sh`

## Testing

Command: `pytest tests/`