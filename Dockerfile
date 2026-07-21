FROM public.ecr.aws/lambda/python:3.12

COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY app.py ${LAMBDA_TASK_ROOT}
COPY routers/ ${LAMBDA_TASK_ROOT}/routers/
COPY schemas/ ${LAMBDA_TASK_ROOT}/schemas/
COPY services/ ${LAMBDA_TASK_ROOT}/services/

CMD ["app.handler"]