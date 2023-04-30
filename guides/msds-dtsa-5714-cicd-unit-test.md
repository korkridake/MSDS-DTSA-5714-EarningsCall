# มาทำ Unit Testing บน Python กันเถอะ !

## CI/CD

Myy GitHub workflow currently has the **workflow_dispatch** event, which allows you to manually trigger a workflow. This is useful for running a workflow on demand, or for testing a workflow before you commit it to your repository.

```
on:
  workflow_dispatch
```

To enable CI/CD for your GitHub workflow, you will need to add a few things to your workflow file. First, you will need to add an on section to your workflow file. This section will define when your workflow should be triggered. In your case, you will want to trigger your workflow on every push to your repository. To do this, you will need to add the following to your on section:

```
on:
  push:
    branches:
      - main
    pull_requests:
      branches:
        - main
```

Next, you will need to add a jobs section to your workflow file. This section will define the jobs that will be run by your workflow. In your case, you will only need one job, which will be responsible for building and pushing your Docker image.

```
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Setup Docker buildx
        uses: docker/setup-buildx-action@79abd3f86f79a9d68a23c75a09a9a85889262adf

      - name: Log into registry ${{ env.REGISTRY }}
        if: github.event_name != 'pull_request'
        uses: docker/login-action@28218f9b04b4f3f62068d7b6ce6ca5b26e35336c
        with:
          registry: ${{ env.REGISTRY }}
          username: kylethedockerate 
          password: ${{ secrets.DOCKERHUB_KEY }}

      - name: Extract Docker metadata
        id: meta
        uses: docker/metadata-action@98669ae865ea3cffbcbaa878cf57c20bbf1c6c38
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}

      - name: Build and push Docker image
        id: build-and-push
        uses: docker/build-push-action@ac9327eae2b366085ac7f6a2d02df8aa8ead720a
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

Once you have made these changes to your workflow file, you can save it and push it to your repository. Once the workflow has been pushed, it will be triggered on every push to your repository. If your workflow is successful, you will see a message in your repository's activity feed that says "Your workflow 'Docker' has completed successfully."

## Additional Resouces on Unit Testing

* [มาทำ Unit Testing บน Python กันเถอะ !](https://www.borntodev.com/2020/04/07/%E0%B8%A1%E0%B8%B2%E0%B8%97%E0%B8%B3-unit-testing-%E0%B8%9A%E0%B8%99-python-%E0%B8%81%E0%B8%B1%E0%B8%99/)
* [ทดสอบโค้ดโปรแกรมภาษาไพทอนด้วย pytest ~ Python 3](https://python3.wannaphong.com/2015/08/pytest.html)
* [Testing a Flask framework with Pytest | CircleCI](https://circleci.com/blog/testing-flask-framework-with-pytest/)
* [po5i/flask-mini-tests](https://github.com/po5i/flask-mini-tests/tree/master)

## Aditional Resources on CI/CD

* 