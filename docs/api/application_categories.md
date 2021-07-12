# Table of Contents

* [nimbleclient.v1.api.application\_categories](#nimbleclient.v1.api.application_categories)
  * [ApplicationCategory](#nimbleclient.v1.api.application_categories.ApplicationCategory)

<a name="nimbleclient.v1.api.application_categories"></a>
# nimbleclient.v1.api.application\_categories

<a name="nimbleclient.v1.api.application_categories.ApplicationCategory"></a>
## ApplicationCategory

```python
class ApplicationCategory(Resource)
```

Provides the list of application categories that are available, to classify volumes depending on the applications that use them.

__Parameters__

- __id             __: Identifier for the application category.
- __name           __: Name of application category.
- __dedupe_enabled __: Specifies if dedupe is enabled for performance policies associated with this application category.
- __creation_time  __: Time when this application category was created.
- __last_modified  __: Time when this application category was last modified.

