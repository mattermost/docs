#!/bin/bash

CNG_REGISTRY=${CNG_REGISTRY:-"registry.gitlab.com/gitlab-org/build/cng"}

GITLAB_VERSION=$(awk '/^appVersion:/ {print $2}' Chart.yaml)
if [ "${GITLAB_VERSION}" == "master" ]; then
  echo "Chart specifies master as GitLab version. Hence not waiting for images."
  exit 0
fi

#TODO: Get all the components and their corresponding versions
components=(gitlab-rails-ee gitlab-unicorn-ee gitlab-workhorse-ee gitlab-sidekiq-ee gitlab-task-runner-ee)

for component in "${components[@]}"; do
  image="${CNG_REGISTRY}/${component}:v${GITLAB_VERSION}"
  echo -n "Waiting for ${image}: "
  while ! $(DOCKER_CLI_EXPERIMENTAL=enabled docker manifest inspect "${image}" > /dev/null 2>&1 ) ; do
    echo -n ".";
    sleep 1m;
  done
  echo "Found"
done
