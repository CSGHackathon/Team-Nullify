#!/bin/sh
npm cache clean && bower cache clean && rm -Rf dist/ node_modules/ bower_components/ tmp/ && npm install && bower install && ember build && ember s
