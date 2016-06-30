var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var autoprefixer = require('gulp-autoprefixer');
var livereload = require('gulp-livereload');
var browserify = require('gulp-browserify');
var uglify = require('gulp-uglify');


var config = {
  script: {
    source : 'src/scripts/main.js',
    watch: 'src/scripts/**/*.js',
    output : 'static/script'
  },
  style : {
    source : 'src/style/*.scss',
    output : 'static/css'
  },
  templates: {
    watch : 'templates/*'
  }
};

/* Compile Our Sass */
gulp.task('sass', function() {
    return gulp.src(config.style.source)
        .pipe(sass())
        .pipe(autoprefixer())
        .pipe(gulp.dest(config.style.output))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifycss())
        .pipe(gulp.dest(config.style.output))
        .pipe(gulp.dest(config.style.output))
        .pipe(livereload());
});

gulp.task('browserify-client', function() {
  return gulp.src(config.script.source)
    .pipe(browserify({
      insertGlobals: true
    }))
    .pipe(rename('bundle.js'))
    .pipe(gulp.dest(config.script.output))
    .pipe(gulp.dest(config.script.output));
});

/* Watch Files For Changes */
gulp.task('watch', function() {
    livereload.listen();
    gulp.watch(config.style.source , ['sass']);
    gulp.watch(config.script.watch, ['browserify-client']);

    /* Trigger a live reload on any Django template changes */
    gulp.watch(config.templates.watch).on('change', livereload.changed);

});

gulp.task('default', ['sass', 'watch']);
