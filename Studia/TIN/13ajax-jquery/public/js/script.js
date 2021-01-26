/* jshint browser: true, devel: true, unused: true, globalstrict: true */
/* global $: false */


'use strict';

var goRoot = function(){
      $('h1').removeClass('clickable').click(null);
      $('nav').removeClass('small');
      $('form').css('display', 'none');
      $('section h2').css('display', 'none');
      $('section ul').remove();
};

function getShowGenre(genre){
   return function(){
         $.getJSON('/genre/'+ genre, function(data, status){
            if(status == 'success'){
               $('nav').addClass('small');
               $('h1').addClass('clickable').click(goRoot);
               $('form').css('display', 'block');
               $('section ul').remove();
               var ul=$('<ul></ul>');
               $.each(data, function(index, value){
                  var li=$('<li></li>').append(
                     $('<span></span>').addClass('author').text(value[1] + ':'),
                     ' ',                          
                     $('<span></span>').addClass('title').text(value[0])
                  );
                  ul.append(li);
               });
               $('section h2').css('display', 'block').text(genre).after(ul);
            }
            else alert(status);
         });
   };
}

var postBook=function(){
   var titleInput=$('input', this).eq(0);
   var authorInput=$('input', this).eq(1);
   var newTitle=titleInput.val();
   var newAuthor=authorInput.val();
   alert('New title: \t\t'+newTitle+'\nNew author: \t'+newAuthor);
   titleInput.val('');
   authorInput.val('');
   return false;
};

var setup = function() {
   $('form').submit(postBook);
   $.getJSON('/genres', function(data, status){
      if(status == 'success'){
         $.each(data, function(index, value){
            var li = $('<li></li>').text(value).addClass('clickable').click(getShowGenre(value));
            $('nav ul').append(li);
         });
      }
      else alert(status);
   });
};
   
$(document).ready(setup);
/* jshint browser: true, devel: true, unused: true, globalstrict: true */
/* global $: false */
'use strict';

var goRoot = function(){
      $('h1').removeClass('clickable').click(null);
      $('nav').removeClass('small');
      $('form').css('display', 'none');
      $('section h2').css('display', 'none');
      $('section table').remove();
};

function getShowGenre(genre){
   return function(){
         $.getJSON('/genre/'+ genre, function(data, status){
            if(status == 'success'){
               $('nav').addClass('small');
               $('h1').addClass('clickable').click(goRoot);
               $('form').css('display', 'block').attr('action', '/');
               $('section table').remove();
               var tab=$('<table></table>');
               $.each(data, function(index, value){
                  var tr=$('<tr></tr>').append(
                     $('<td></td>').addClass('author').text(value[1] + ':'),
                     ' ',                          
                     $('<td></td>').addClass('title').text(value[0])
                  );
                  tab.append(tr);
               });
               $('section h2').css('display', 'block').text(genre).after(tab);
               checkLogin();
            }
            else alert(status);
         });
   };
}

function reloadGenres(genre){
      $.getJSON('/genre/'+ genre, function(data, status){
            if(status == 'success'){
                  var tab=$('section table');
                  tab.children('tbody').children('tr').remove();
                  $.each(data, function(index, value){
                        var tr=$('<tr></tr>').append(
                              $('<td></td>').addClass('author').text(value[1] + ':'),
                              ' ',     
                               $('<td></td>').addClass('title').text(value[0])
                        );
                        tab.append(tr);
                  });
            checkLogin();
            }
            else alert(status);
         });
}

function getTable(genre){
      $.getJSON('/genre/'+ genre, function(data, status){
            if(status == 'success'){
               var tab=$('<table></table>');
               $.each(data, function(index, value){
                  var tr=$('<tr></tr>').append(
                     $('<td></td>').addClass('author').text(value[1] + ':'),
                     ' ',                          
                     $('<td></td>').addClass('title').text(value[0])
                  );
                  tab.append(tr);
               });
               $('section h2').css('display', 'block').text(genre).after(tab);
            }
            else alert(status);
         });
}

function loginRedirect(genre){
      $('input#genre').remove();
      $('h2').text(genre);
      $('form').unbind().submit(postBook);
      var inputs = $('form p input');
      inputs.eq(0).removeAttr('name');
      inputs.eq(1).removeAttr('name');
      inputs.eq(2).attr('value', 'Dodaj książkę');
      var spanNodes = inputs.siblings('span');
      spanNodes.eq(0).text('Tytuł: ');
      spanNodes.eq(1).text('Autor: ');
      getTable(genre);
      checkLogin();      
}

function setMessage(text, id){
      var divMessageNode = jQuery('<div/>', {
            class: 'message',
            id: id,
            text: text
      }).appendTo('footer');
      divMessageNode.fadeIn(300).fadeOut(2500);
      setTimeout(function() {
             $('.message').remove();
      }, 3600);
}

var login = function(event) {
       event.preventDefault();
       var form = $('form');
       var loginInput=$('input', this).eq(0);
       var passwordInput=$('input', this).eq(1);
       var genreInput=$('input', this).eq(3);
       var login = loginInput.val();
       var password = passwordInput.val();
       var genre = genreInput.val();
       var url = '/login';
       var data = {'login': login, 'password': password};
       $.post( url, data)
       .done(function() {
            setMessage('Zalogowałeś się!', 'message');
            loginRedirect(genre);
       })
       .fail(function() {
            setMessage('Błędny login lub hasło!', 'loginError');
            loginPage(genre);
      });
       loginInput.val('');
       passwordInput.val('');
       return false;
}

var logout = function(){
      $.post('/logout')
            .done(function(){
                  $('button.logout').remove();
                  goRoot();
                  setMessage('Wylogowałeś się!', 'logout');
            })
} 

function checkLogin(){
      var result = '';
      $.post('/checkLogin')
            .done(function(){
                  var buttons = $('button.logout');
                  if(buttons.length === 0) $('<button>Wyloguj się</button>').addClass('logout').click(logout).prependTo('footer');
            })
            .fail(function(){
                  $('button.logout').remove();
            })
}

function loginPage(genre){
      $('h2').text('Zaloguj się');
      $('section table').remove();
      var form = $('form');
      form.unbind().submit(login);
      var spans = $('form p span');
      spans.eq(0).text('Login: ');
      spans.eq(1).text('Hasło: ');
      var inputs = $('form p input');
      inputs.eq(0).attr('name', 'username');
      inputs.eq(1).attr('name', 'password');
      inputs.eq(2).val('Zaloguj się');
      $('<input>').attr({
            type: 'hidden',
            id: 'genre',
            value: genre
      }).appendTo('form');
}

var postBook=function(event){
       event.preventDefault();
       var genre = $('h2').html();
       var titleInput=$('input', this).eq(0);
       var authorInput=$('input', this).eq(1);
       var newTitle=titleInput.val();
       var newAuthor=authorInput.val();
       var url = '/genre/'+genre;
       var data = {'newTitle': newTitle, 'newAuthor': newAuthor};
       $.post( url, data)
       .done(function() {
            setMessage('Pomyślnie dodano książkę!', 'message');
            reloadGenres(genre);
       })
       .fail(function() {
            loginPage(genre);
      });
       titleInput.val('');
       authorInput.val('');
       return false;
};

var setup = function() {
   $('form').submit(postBook);
   $.getJSON('/genres', function(data, status){
      if(status == 'success'){
         $.each(data, function(index, value){
            var li = $('<li></li>').text(value).addClass('clickable').click(getShowGenre(value));
            $('nav ul').append(li);
         });
         checkLogin();
      }
      else alert(status);
   });
};

var auth = function(req, res, next) {
  if (req.session && req.session.user === "admin" && req.session.pass === 'nimda')
    return next();
  else
    return res.sendStatus(401);
};
   
$(document).ready(setup);