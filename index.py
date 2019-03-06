def handler(event, context):
    template = event["fragment"]
    params = event["templateParameterValues"]
    transform_param = params['TransformString']
    fragment = {}  # TODO
    fragment['AttributeDefinitions'] = [
        {'AttributeName': transform_param, 'AttributeType': 'S'}]
    fragment['KeySchema'] = [
        {'AttributeName': transform_param, 'KeyType': 'HASH'}]
    fragment['BillingMode'] = 'PAY_PER_REQUEST'

    return {
        "requestId": event["requestId"],
        "status": "success",
        "fragment": fragment}
