/*global module:false*/
module.exports = function(grunt) {

  'use strict';

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    meta : {
      banner : '/*!\n' +
      ' * GMaps.js v<%= pkg.version %>\n' +
      ' * <%= pkg.homepage %>\n' +
      ' *\n' +
      ' * Copyright <%= grunt.template.today("yyyy") %>, <%= pkg.author %>\n' +
      ' * Released under the <%= pkg.license %> License.\n' +
      ' */\n\n'
    },

    concat: {
      options: {
        banner: '<%= meta.banner %>'
      },
      dist: {
        src: [
          'mongo/gmaps.core.js',
          'mongo/gmaps.controls.js',
          'mongo/gmaps.markers.js',
          'mongo/gmaps.overlays.js',
          'mongo/gmaps.geometry.js',
          'mongo/gmaps.layers.js',
          'mongo/gmaps.routes.js',
          'mongo/gmaps.geofences.js',
          'mongo/gmaps.static.js',
          'mongo/gmaps.map_types.js',
          'mongo/gmaps.styles.js',
          'mongo/gmaps.streetview.js',
          'mongo/gmaps.events.js',
          'mongo/gmaps.utils.js',
          'mongo/gmaps.native_extensions.js'
        ],
        dest: 'gmaps.js'
      }
    },

    jasmine: {
      options: {
        template: 'test/template/jasmine-gmaps.html',
        specs: 'test/spec/*.js',
        vendor: 'http://maps.google.com/maps/api/js?sensor=true',
        styles: 'test/style.css'
      },
      src : '<%= concat.dist.src %>'
    },

    watch : {
      files : '<%= concat.dist.src %>',
      tasks : 'default'
    },

    jshint : {
      all : ['Gruntfile.js']
    },

    uglify : {
      options : {
        sourceMap : true
      },
      all : {
        files: {
           'gmaps.min.js': [ 'gmaps.js' ]
        }
      }
    },

    umd : {
      all : {
        src : 'gmaps.js',
        objectToExport : 'GMaps',
        globalAlias : 'GMaps',
        template : 'umd.hbs',
        deps: {
          amd: ['jquery', 'googlemaps!']
        }
      }
    }

  });

  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-jasmine');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-umd');

  grunt.registerTask('test', ['jshint', 'jasmine']);
  grunt.registerTask('default', ['test', 'concat', 'umd', 'uglify']);
};
