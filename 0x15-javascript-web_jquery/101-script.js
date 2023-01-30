$(document).ready(
  function () {
    const unorderedList = $('UL.my_list');
    const listElement = '<li>Item</li>';

    $('DIV#add_item').click(function () {
      $(unorderedList).append(listElement);
    });

    $('DIV#remove_item').click(function () {
      $('UL.my_list li:last-child').remove();
    });

    $('DIV#clear_list').click(function () {
      $(unorderedList).empty();
    });
  }
);
