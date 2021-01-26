module.exports = function (grunt) {
    grunt.loadNpmTasks('grunt-contrib-compress');
    grunt.loadNpmTasks('grunt-contrib-rename');
    grunt.initConfig({
        compress: {
            main: {
                options: {
                    archive: 'czat.zip'
                },
                files: [{
                    src: ['package.json', 'serwer.js', 'public/**']
                }]
            }
        },
        rename: {
            main: {
               files: [
                           {src: ['czat.zip'], dest: 'czat.pdf'},
                  ]
            }
         }    });
    grunt.registerTask('default', ['compress', 'rename']);

};
